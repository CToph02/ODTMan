from rest_framework import status
from rest_framework.response import Response

class MessageResponseMixin:
    verbose_name = None

    def get_verbose_name(self):
        if self.verbose_name:
            return self.verbose_name
        return self.get_serializer().Meta.model._meta.verbose_name.capitalize()
    
    def perform_create(self, serializer):
        instance = serializer.save()
        self.created_object_name = str(instance)
    
    def perform_update(self, serializer):
        instance = serializer.save()
        self.created_object_name = str(instance)
    
    def perform_destroy(self, instance):
        self.created_object_name = str(instance)
        instance.delete()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        verbose = self.get_verbose_name()

        return Response(
            {
                'message': f"{verbose} {self.created_object_name} has been successfully created.",
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)        
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        verbose = self.get_verbose_name()

        return Response(
            {
                'message': f"{verbose} {self.created_object_name} has been successfully updated.",
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(instance)

        self.perform_destroy(instance)

        verbose = self.get_verbose_name()

        return Response(
            {
                'message': f"{verbose} {self.created_object_name} has been successfully deleted.",
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )