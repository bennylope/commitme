==========
Commit me!
==========

Removes model instance `save` calls from Django model methods.

A typical Django model method::

    class SomeModel(models.Model):

        def method(self):
            # do things, maybe return something!
            self.save()

This is no fun. If we want to test our model method now we have
to get the database involved. Not to mention if you've got a bunch of methods
like this you can easily end up with boilerplate like this::

    class SomeModel(models.Model):

        def method(self, commit=True):
            # do things, maybe return something!
            if commit:
                self.save()

Or maybe just I do. Because surely you want to be able to control saving to the
database, for testing if nothing else.

Instead, just apply the `commitme.save` decorator with a default commit
value::

    class SomeModel(models.Model):

        @commitme.save(True)
        def method(self):
            # do things, maybe return something!

Now the instance will be saved and this can always be toggled using the
`commit` keyword argument.::

    result = some_model_instance.method(commit=True)

Or don't save it.::

    result = some_model_instance.method(commit=False)

But let your method just do the things you need it to do.

