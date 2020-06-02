#- Custom Displayables & Graphics --------------------------------------
#
# @note{{{
#   You'll need the **00functions.rpy** and **02store.rpy** files in order
#   to use the classes defined here.
# }}}
#
# Ren'Py ships with a handful of displayable objects, which fits quite a
# lot of use cases. As for **Cute Demon Crashers!**, we wanted to have
# the equivalent of the built-in `ConditionSwitch`, but which could use
# transitions between each state.
#
# The side image is actually the only place where using something like
# `ConditionSwitch` would be absolutely required, but in all other
# places it would cut down the amount of work (and image tags!) by quite
# a lot, since we've got a plethora of variants for eyes, mouths, and
# all sorts of parts that compose a character's sprite.
#
# In light of this, the ideal solution was to write a new displayable
# that works in a way very similar to `ConditionSwitch`, but that allows
# transitions to be defined when moving from one state to another. The
# custom `StateMachineDisplayable` does this by encoding a kind of
# @link("Finite State Machine"), where one may provide an additional
# transition when moving between states. Unlike `ConditionSwitch`,
# however, moving between states in the `StateMachineDisplayable` is
# explicit, and this comes with the nice side-effect of being able to
# provide different transitions at different points in time.
#
# Furthermore, while the `StateMachineDisplayable` can only handle one
# state at a given time (so, for example, it could only be used for a
# single layer in a image), the `ComposedSprite` object makes up for
# that by providing the analogous of `LiveComposite` for
# `StateMachineDisplayable`s.
#
# @ref("Finite State Machine"): http://en.wikipedia.org/wiki/Finite-state_machine
init -100 python:

    ### class: StateMachineDisplayable() < renpy.Displayable, StoreBackedObject
    #
    # The `StateMachineDisplayable` allows one to have a displayable
    # that changes throughout the time. It operates as a
    # @link("Finite State Machine"), in which there are several possible
    # states that it might be, but only one of those can be active at
    # any given time.
    #
    # Each state has an associated Ren'Py displayable, which will be
    # shown when that this object reaches that state, and transitions
    # may be provided for moving from one state to another.
    #
    #
    # --- Creating StateMachineDisplayables ----------------------------
    #
    # To create a `StateMachineDisplayable`, one needs to pass in an
    # unique name for the displayable, the initial state of the
    # displayable, and a mapping of states to other Ren'Py displayables,
    # which will constitute the possible states that the displayable
    # might ever be in its lifetime.
    #
    # The unique name is used to store the current state of the
    # displayable in a way that's compatible with Ren'Py's
    # save/load/rollback mechanism. See `02store.rpy` for more
    # information.
    #
    # @example("py" caption: "Creating a StateMachineDisplayable"){{{
    #   claire_base = StateMachineDisplayable(
    #     "claire_base",        # An unique name for this displayable
    #     "default",            # The initial state for this displayable
    #     # A mapping of "state": displayable
    #     {
    #       "default": "assets/sprites/claire/cl_base_clothed.png",
    #       "lazy": "assets/sprites/claire/cl_base/lazy.png",
    #       "chemise": "assets/sprites/claire/cl_base_chemise.png"
    #     }
    #   )
    # }}}
    #
    #
    # --- Showing and moving between states ----------------------------
    #
    # You can change the current state of a `StateMachineDisplayable` by
    # calling the `set_state` method and passing in the new state (and
    # optionally a transition to be used when showing the new
    # displayable).
    #
    # @example("py" caption: "Showing and switching states"){{{
    #   $ claire_base.set_state("lazy")
    #   show claire_base with dissolve
    #   "I feel so lazy today..."
    #   $ claire_base.set_state("default", transition=Dissolve(1.0, alpha=True))
    #   "Why must I change? I just want to stay in bed all day..."
    # }}}
    #
    # Another method in the `StateMachineDisplayable` class is
    # `snapshot`, which gives you the displayable associated with a
    # particular state. This was introduced here primarily so we could
    # show the CGs that are constructed with this class in the gallery
    # in a simpler way.
    #
    # @example("py" caption: "StateMachineDisplayable snapshots"){{{
    #   image claire lazy = claire_base.snapshot("lazy")
    #   $ claire_base.set_state("default")
    #   show claire lazy at left        # Still the correct `lazy` displayable
    #   show claire_base at right
    # }}}
    class StateMachineDisplayable(renpy.Displayable, StoreBackedObject):

        #### method: __init__(slot, initial_state, states, **kwargs)
        # @type: str, α, { α: Displayable } -> unit
        #
        # Initialises a `StateMachineDisplayable` instance.
        def __init__(self, slot, initial_state, states, **properties):
            # Ren'Py's core displayable classes must be called with the
            # additional displayable properties (like style things and
            # what not).
            super(StateMachineDisplayable, self).__init__(**properties)

            # Since this class also uses `StoreBackedObject` to properly
            # handle Ren'Py's save/loading/rollback system, we need to
            # initialise that with an unique slot. We prepend
            # `smd_state__` to the provided slot so it won't collide
            # with other variables/StoreBackedObject classes.
            StoreBackedObject.__init__(self, "smd_state__" + slot)

            # A `Transition` object needs to be provided with two
            # displayables, *old* and *new*, it then transitions from
            # the old displayable to the new one.
            #
            # We keep track of the old state of this object in the
            # `old_state` field, then dynamically compute which
            # displayable was that from the state mapping. This assumes
            # that `states` never changes.
            self.old_state = None

            # Since Ren'Py can rollback, and we only keep track of the
            # current state in the store, we need to make sure we don't
            # show incorrect transitions when rolling back/forward. Just
            # keeping track of the `current_state` is sufficient for
            # that, but the core of this is done in the `per_interact`
            # method.
            self.current_state = None

            # The mappings of *state* to *displayable* are stored in the
            # `states` field. We assume this field never changes.
            self.states = states

            # At any point in time we'll be showing a displayable to the
            # user. This may be a transition, if we've just changed the
            # state in this interaction, or a regular displayable.
            #
            # The `transition` field stores the transition we're showing
            # the user in this interaction, in response to a `set_state`
            # call.
            self.transition = None

            # The `displayable` field stores the displayable associated
            # with the current state of the displayable, and we fallback
            # to showing just this when no transition is being shown.
            self.displayable = None

            # Furthermore we need to keep track of the transition's
            # shown/animation times, so we pass the correct values when
            # rendering it.
            self.shown_time = 0
            self.anim_time = 0

            # We use the `reset` field to keep track of when we've
            # changed states, so we can update the `shown_time` and
            # `anim_time` values accordingly and get the transition
            # animation to play correctly.
            self.reset = False

            # Finally, we move this displayable to the provided initial
            # state, so it's ready to be shown on the screen.
            self.set_state(initial_state)


        #### method: snapshot([state=None])
        # @type: a -> Displayable
        #
        # Returns the displayable associated with the provided state in
        # this object. Fallsback to the current state if no state is
        # provided, and finally to the `Null` displayable if we can't
        # find any displayable in the state mapping.
        def snapshot(self, state=None):
            if state is None:
                state = self.current_state
            return self.states.get(state) or Null()


        #### method: redraw()
        # @type: unit -> unit
        #
        # Forces this displayable to redraw itself with the new state
        # information. Usually called after moving states, or new
        # interactions.
        def redraw(self):
            self.reset = True
            renpy.redraw(self, 0)


        #### method: set_state(new_state[, transition=None])
        # @type: a, Transition -> unit
        #
        # Transitions to the provided new state, optionally with a nice
        # transition animation.
        #
        # We'll construct a transition by changing from the current
        # state (which is loaded from the Ren'Py store) to the new
        # one. If we can't get a displayable for either, we use the
        # `Null` displayable, which means we don't get any transition
        # for things like Dissolve.
        #
        # This also updates the store with the new state, so state
        # changes works properly with rollbacks and loading.
        def set_state(self, new_state, transition=None):
            self.current_state = new_state
            self.old_state = self.load()
            self.store(new_state)

            old_d = self.states.get(self.old_state) or Null()
            cur_d = renpy.easy.displayable(self.states.get(new_state) or Null())
            self.displayable = cur_d
            self.transition = anim.TransitionAnimation(old_d, 0.0, transition, cur_d)
            self.redraw()


        #### method: state()
        # @type: () -> any
        #
        # Returns the current state of the displayable.
        def state(self):
            return self.load()


        #### method: per_interact()
        # @type: unit -> unit
        #
        # Ren'Py calls `per_interact` internally every time a new
        # interaction begins. This gives us a chance of showing the
        # proper state to the user in case of rollbacks.
        def per_interact(self):
            new_state = self.load()

            # To avoid creating displayables unecessarily, we only call
            # `set_state` when the new state is really a **new** state.
            if self.current_state != new_state:
                self.set_state(new_state)

            # Also, in order to avoid showing the wrong transition to
            # people, we get rid of it in new interactions.
            if renpy.is_start_interact() and not self.reset:
                self.transition = None
                self.redraw()


        #### method: current_displayable()
        # @type: unit -> Displayable
        #
        # Returns the displayable that should be shown to the user in
        # this interaction.
        def current_displayable(self):
            return self.transition or self.displayable


        #### method: render(width, height, st, at)
        # @type: int, int, int, int -> renpy.Render
        #
        # Renders the current displayable so Ren'Py can show it on the
        # screen.
        def render(self, width, height, st, at):
            # We need to reset the times if this is the first time we're
            # showing this state, so transitions/animations work
            # correctly.
            if self.reset:
                self.reset = False
                self.shown_time = st
                self.anim_time = at

            d = self.current_displayable()
            if d:
                return renpy.render(d,
                                    width,
                                    height,
                                    st - self.shown_time,
                                    at - self.anim_time)
            else:
                return renpy.Render(0, 0)

        #### method: visit()
        # @type: unit -> list(Displayable)
        #
        # Ren'Py uses this list to predict images and stuff.
        def visit(self):
            return [self.transition, self.displayable]


    ### class: ComposedSprite()
    #
    # Since `StateMachineDisplayable` only deals with a single
    # displyable at a time, like `ConditionSwitch`, we need a way of
    # composing several of them to form a single displayable. One could
    # just use `LiveComposite`, but then they would need to call
    # `set_state` on each of the parts, one at a time. To solve this,
    # `ComposedSprite` bundles several displayables into a single thing,
    # one of which may be a `StateMachineDisplayable`, and allows one to
    # change the state of several parts with a single command.
    #
    #
    # --- Creating ComposedSprites -------------------------------------
    #
    # To construct a `ComposedSprite`, one needs to pass in the size of
    # the final image, as a `(width, height)` tuple, and a series of
    # "layers", as a `(layer name, (x offset, y offset), displayable)`
    # tuple. This is very similar to what `LiveComposite` expects,
    # except that we accept an additional `layer name` value for
    # displayables that are `StateMachineDisplayable`.
    #
    # The `layer name` may be a string that provides an unique name for
    # that layer in this `ComposedSprite` displayable, or `None` if the
    # displayable in that layer isn't a `StateMachineDisplayable`.
    #
    # @example("py" caption: "Creating a ComposedSprite"){{{
    #   glasses_claire = ComposedSprite(
    #     (360, 504),
    #     ("base", (0, 0), claire_base),
    #     ("eyes", (0, 0), claire_eyes),
    #     ("mouth", (0, 0), claire_mouth),
    #     (None, (0, 0), "assets/sprites/claire/cl_glasses.png")
    #   )
    # }}}
    #
    #
    # --- Showing ComposedSprites & moving between states --------------
    #
    # Since `ComposedSprite` isn't a displayable itself, you can't show
    # it directly on the screen. Instead, it gives you two methods to
    # create displayables from the initial `ComposedSprite`
    # description. In both cases the layers are composed in the order
    # they're given, where the first ones are at the very bottom of the
    # image, and last ones are at the very top of the image.
    #
    # The `displayable` method gives you a live displayable, which
    # reflects the current state of all `StateMachineDisplayable`s that
    # constitute the image:
    #
    # @example("py" caption: "Using .displayable() to show ComposedSprites"){{{
    #   image claire glasses = glasses_claire.displayable()
    #   show claire glasses with dissolve
    # }}}
    #
    # Similar to `StateMachineDisplayable`, you can use a `set_state`
    # method in the `ComposedSprite` object to change the current state
    # of the `ComposedSprite`, but here you'll need to pass in a mapping
    # of which layers you want the state to change. A transition
    # argument may be likewise provided:
    #
    # @example("py" caption: "Moving between states in ComposedSprites"){{{
    #   show claire glasses with dissolve
    #   $ glasses_claire.set_state(base="lazy", transition=dissolve)
    #   "Hello."
    #   $ glasses_claire.set_state(eyes="happy", mouth="kitty")
    #   "'Tis nice to see ya."
    # }}}
    #
    # Another way of getting a displayable out of a `ComposedSprite` is
    # to use the `snapshot` method. This again works in a similar
    # fashion to `StateMachineDisplayable`'s `snapshot` method, except
    # that it takes mappings from layers to states, and gives you back a
    # proper (static) composition of all those layers.
    #
    # @example("py" caption: "Snapshots in ComposedSprites"){{{
    #   image claire kitty = glasses_claire.snapshot(eyes="happy", mouth="kitty")
    #   show claire glasses at left
    #   show claire kitty at right
    #   # This will only affect the `claire glasses` image.
    #   $ glasses_claire.set_state(mouth="grin")
    # }}}
    class ComposedSprite(object):

        #### method: __init__(size, *layers)
        # @type: (int, int), (str | None, (int, int), Displayable)... -> unit
        #
        # Initialises an instance of `ComposedSprite`
        def __init__(self, size, *layers):
            # We use `LiveComposite` for composing the sprites, so we
            # need to know the size of the final image beforehand.
            self.size = size

            # The layers this `ComposedSprite` has, as a list.
            self.layers = layers

            # The `layer_map` helps us to easily set the state of
            # `StateMachineDisplayable` layers, by mapping layer names
            # directly to those objects.
            self.layer_map = {}
            for (name, _, displayable) in layers:
                if name is not None:
                    self.layer_map[name] = displayable


        #### method: set_state([transition=None, ] **kwargs)
        # @type: Transition, { str: any } -> unit
        #
        # Changes the state of all layers provided by the mappings.
        def set_state(self, transition=None, **kwargs):
            for key in kwargs:
                self.layer_map[key].set_state(kwargs[key], transition)


        #### method: state()
        # @type: () -> (any...)
        #
        # Returns a tuple of the states used for the object, ignoring
        # states that have no names.
        def state(self):
            return tuple([d.state() for (name, _, d) in self.layers if name is not None])


        #### method: dict_to_state_tuple(dict)
        # @type: { string -> any } -> (any...)
        #
        # Returns a tuple of states in the correct order from the given dictionary.
        def dict_to_state_tuple(self, dict):
            return tuple([dict[name] for (name, _, _) in self.layers if name is not None])


        #### method: snapshot(**kwargs)
        # @type: { str: any } -> Displayable
        #
        # Returns a static composition of the `ComposedSprite`, as a
        # displayable. *Static* here just means that the resulting image
        # won't be changed by calling `set_state` in any of the layers.
        #
        # This ignores displayables `None` states, and expects that a
        # `snapshot` method, if present, means SMD's snapshot.
        def snapshot(self, **kwargs):
            def get_snapshot(displayable, state):
                if state is not None and callable(getattr(displayable, "snapshot")):
                    return displayable.snapshot(state)
                else:
                    return displayable

            return LiveComposite(
                self.size,
                *flatten([
                    [pos, get_snapshot(displayable, kwargs.get(name))]
                    for (name, pos, displayable) in self.layers
                ])
            )


        #### method: displayable()
        # @type: unit -> Displayable
        #
        # Returns a live displayable for this `ComposedSprite`.
        def displayable(self):
            return LiveComposite(
                self.size,
                *flatten([[pos, displayable] for (_, pos, displayable) in self.layers])
            )

    ### class: Emotion()
    #
    # `ComposedSprite` instances take a dictionary of states for the
    # `StateMachineDisplayable`, and this class makes it easier to create such
    # dictionaries by providing base values for common expressions.
    #
    #
    class Emotion(object):
        @staticmethod
        def normal(**kwargs):
            return merge({ "emotion_base": "default",
                           "eyebrows": "default",
                           "eyes": "default",
                           "mouth": "default",
                           "emotion": "default"
                         }, kwargs)

        @staticmethod
        def shock(**kwargs):
            return Emotion.normal(**merge({ "eyebrows": "flat",
                                            "eyes": "shock",
                                            "mouth": "fun ah",
                                            "emotion": "shock"
                                          }, kwargs))

    #### class: PannableDisplayable()
    #
    # Wrapping an object in a Pannable allows one to create a Viewport-like
    # displayable that's controlled by keyboard and mouse position.
    #
    # The pannable displayable is used in the gallery to allow people to
    # see images that are larger than the screen size.
    class PannableDisplayable(renpy.Displayable):

        ##### method: __init__(displayable, **properties)
        # @type: Displayable -> unit
        #
        # Initialises an instance of `PannableDisplayable`.
        def __init__(self, displayable, **properties):
            super(PannableDisplayable, self).__init__(**properties)

            # The displayable that we'll be showing the user. We assume this
            # displayable is always bigger than the screen size, although there
            # are no problems if it isn't — this displayable is just kind of
            # useless for those cases.
            self.displayable = renpy.displayable(displayable)

            # The `PannableDisplayable` shows two (configurable) "arrows" at
            # the top and bottom of the screen. Hovering the mouse over the areas
            # where these arrows are displayed will pan the displayable towards
            # that direction.
            #
            # We consider 200 pixels at the top and at the bottom of the screen
            # for this area, as shown in the graph below:
            #
            # @code("text"){{{
            #     +---------------------------------------------+  -.
            #     |                (arrow up)                   |   |- 200px
            #     |_____________________________________________|  _,
            #     |                                             |   |
            #     |                                             |   |
            #     |                                             |   |
            #     |              (displayable)                  |   |- 400px
            #     |                                             |   |
            #     |                                             |   |
            #     |_____________________________________________|  _,
            #     |                                             |   |
            #     |               (arrow down)                  |   |- 200px
            #     +---------------------------------------------+  -'
            # }}}
            self.arrow_up = renpy.displayable("assets/ui/pan-up-idle.png")
            self.arrow_up_hover = renpy.displayable("assets/ui/pan-up-hover.png")
            self.arrow_down = renpy.displayable("assets/ui/pan-down-idle.png")
            self.arrow_down_hover = renpy.displayable("assets/ui/pan-down-hover.png")


            # How many pixels we pan the image by each frame.
            self.speed = 10

            # Determines the vertical offset in which to draw the child
            # displayable. Note that this value is always clamped between 0 and
            # this displayable's height.
            self.offset = 0

            # The `height` of this displayable, and the `child_height` of the
            # child displayable. These values are automatically computed when
            # rendering the displayable and shouldn't be changed.
            self.height = 0
            self.child_height = 0

            # Tracks the animation times so we can properly display the child
            # displayable and its animation (if any).
            self.shown_time = 0
            self.anim_time = 0

            # Tracks the direction in which we are panning the image. This is
            # changed when the user places the mouse within the area of one
            # of the arrows. Possible values are `None`, `"up"` and `"down"`.
            self.dir = None


        ##### method: get_render(is_hovered, idle, hover, w, h, st, at)
        # @type: bool, Displayable, Displayable, int, int, int, int -> Displayable
        #
        # A convenience function for returning which arrow to show the user.
        def get_render(self, is_hovered, idle, hover, w, h, st, at):
            if is_hovered:
                return renpy.render(hover, w, h, st, at)
            else:
                return renpy.render(idle, w, h, st, at)

        ##### method: clamped(offset)
        # @type: int -> int
        #
        # Makes sure the offset is no less than 0, and no more than the
        # available height for fitting the child displayable. This ensures
        # that we're always using the entire size of the `PannableDisplayable`
        # to show the child displayable.
        def clamped(self, offset):
            return max(0, min(offset, self.child_height - self.height))


        ##### method: render(width, height, st, at)
        # @type: int, int, int, int -> Render
        #
        # Called by Ren'Py to render the displayable.
        def render(self, width, height, st, at):
            # Update the amount of vertical space we have to show this displayable.
            self.height = height

            # Renders the child displayable and updates the amount of space it's
            # going to take, so we can properly fit it on the screen.
            child = renpy.render(self.displayable, width, height, st, at)
            (cw, ch) = child.get_size()

            self.child_height = ch

            # Renders the child displayable and the proper arrows for panning
            # this displayable.
            render = renpy.Render(width, height)
            render.blit(child, (0, -int(self.offset)))

            arrow_up = self.get_render(self.dir == "up",
                                       self.arrow_up,
                                       self.arrow_up_hover,
                                       width, height, st, at)
            arrow_down = self.get_render(self.dir == "down",
                                         self.arrow_down,
                                         self.arrow_down_hover,
                                         width, height, st, at)

            if self.dir == "up":
                self.offset = self.clamped(self.offset + self.speed)
            if self.dir == "down":
                self.offset = self.clamped(self.offset - self.speed)


            (aw, ah) = arrow_up.get_size()
            mid = height / 2
            render.blit(arrow_up, (width - aw - 20, mid - ah - 200))
            render.blit(arrow_down, (width - aw - 20, mid + 200))

            # Asks Ren'Py to redraw this displayable soon.
            renpy.redraw(self, 0.025)

            return render


        ##### method: event(ev, x, y, st)
        # @type: pygame.event, int, int, int
        #
        # Called by Ren'Py whenever this displayable has a chance to handle
        # some PyGame event. We need this to handle keyboard-based panning
        # (by looking at keys pressed when focusing this displayable), and
        # mouse pointer-based panning, by looking at the x,y coordinates
        # of the mouse pointer.
        def event(self, ev, x, y, st):
            mid = self.height / 2

            if renpy.display.behavior.map_event(ev, "focus_up"):
                self.dir = "up"
            elif renpy.display.behavior.map_event(ev, "focus_down"):
                self.dir = "down"
            elif y < mid - 200:
                self.dir = "up"
            elif y > mid + 200:
                self.dir = "down"
            elif self.dir is not None:
                self.dir = None

            renpy.redraw(self, 0)
            return super(PannableDisplayable, self).event(ev, x, y, st)


        ##### method: visit()
        # @type: unit -> list(Displayable)
        #
        # Ren'Py uses this list to predict images and stuff.
        def visit(self):
            return [self.displayable]
