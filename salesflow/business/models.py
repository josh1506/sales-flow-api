from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Business(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    country = models.CharField(max_length=255, null=False, blank=False)
    owner = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name="owned_business")
    manager = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="manager_business")
    assistant_manager = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, related_name="assistant_manager_business"
    )
    date_created = models.DateTimeField(auto_now=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    user_created = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, related_name="created_business"
    )
    user_updated = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, related_name="updated_business"
    )
    user_deleted = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, related_name="deleted_business"
    )

    def __str__(self):
        return self.name
