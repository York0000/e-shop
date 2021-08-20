from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class PostTagModel(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class PostModel(models.Model):
    title = models.CharField(max_length=512)
    image = models.ImageField(upload_to='posts')
    banner = models.ImageField(upload_to='post_banners')
    content = RichTextUploadingField()
    author = models.ForeignKey(
        AuthorModel,
        on_delete=models.PROTECT,
        related_name='posts'
    )
    tags = models.ManyToManyField(
        PostTagModel,
        related_name='posts'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def get_comments(self):
        return self.comments.order_by('-created_at')


class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
