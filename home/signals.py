from django.db.models.signals import post_delete, post_save, pre_delete, pre_save
from django.dispatch import receiver
from home.models import Article

@receiver(post_save, sender=Article)
def article_post_save(sender, instance, created, **kwargs):
    if created:
        print(f'Article "{instance.title}" has been created.')
    else:
        print(f'Article "{instance.title}" has been updated.')

@receiver(pre_save, sender=Article)
def article_pre_save(sender, instance, **kwargs):
    print(f'About to save Article "{instance.title}".')

# @receiver(post_delete, sender=Article)
# def article_post_delete(sender, instance, **kwargs):
#     print(f'Article "{instance.title}" has been deleted.')

# @receiver(pre_delete, sender=Article)
# def article_pre_delete(sender, instance, **kwargs):
#     print(f'About to delete Article "{instance.title}".')

@receiver(pre_delete, sender=Article)
def article_pre_delete(sender, instance, **kwargs):
    a=4/0
    print(a)
    print(f"Article '{instance.title}' is about to be deleted.")


@receiver(post_delete, sender=Article)
def article_post_delete(sender, instance, **kwargs):
    print(f"Article '{instance.title}' is deleted.")