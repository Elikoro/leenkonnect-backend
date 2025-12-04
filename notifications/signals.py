from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# Import models lazily inside signal handlers to avoid circular imports at import time.
User = get_user_model()


@receiver(post_save, sender=None)
def ticket_assignment_notification(sender, instance, created, **kwargs):
    """Create a notification when a Ticket is created and assigned.

    The sender is set dynamically when connecting in ready() to avoid importing
    tickets.models at module import time and to prevent circular imports.
    """
    # Ensure this handler only runs for Ticket instances
    if instance.__class__.__name__ != "Ticket":
        return

    assignee = getattr(instance, "assigned_to", None)
    if created and assignee:
        from .models import Notification

        Notification.objects.create(
            user=assignee,
            organization=getattr(instance, "organization", None),
            title="New Ticket Assigned",
            message=f"You have been assigned Ticket #{instance.id}.",
            type="info",
            related_type="ticket",
            related_id=instance.id,
        )


@receiver(pre_save, sender=None)
def _project_pre_save(sender, instance, **kwargs):
    if instance.__class__.__name__ != "Project":
        return

    if instance.pk:
        try:
            from projects.models import Project as ProjectModel

            instance._old_status = ProjectModel.objects.get(pk=instance.pk).status
        except Exception:
            instance._old_status = None


@receiver(post_save, sender=None)
def project_status_change_notification(sender, instance, created, **kwargs):
    if instance.__class__.__name__ != "Project":
        return

    old_status = getattr(instance, "_old_status", None)
    if not created and old_status is not None and old_status != instance.status:
        from .models import Notification

        Notification.objects.create(
            title="Project Updated",
            message=f"Project '{getattr(instance, 'title', getattr(instance, 'name', ''))}' moved to {instance.status}.",
            related_type="project",
            related_id=instance.id,
            organization=getattr(instance, "organization", None),
        )
