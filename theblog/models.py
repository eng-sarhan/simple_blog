from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def get_absolute_url(self):
        return reverse("author", args=[str(self.id)])

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('theblog:home')

    class Meta:
        verbose_name_plural = "categories"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    # title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category, default='Science')
    # snippet = models.CharField(max_length=255, blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('theblog:article-detail', args=(str(self.id)))
        return reverse('theblog:home')

    # class Comment(models.Model):
    #     post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    #     name = models.CharField(max_length=255)
    #     body = models.TextField()
    #     date_added = models.DateTimeField(auto_now_add=True)
    #
    #     def __str__(self):
    #         return '%s - %s' % (self.post.title, self.name)

    def get_update_url(self):
        return reverse('theblog:update_post', kwargs={
            'pk': self.pk
        })

    def get_delete_url(self):
        return reverse('theblog:delete_post', kwargs={
            'pk': self.pk
        })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-date_added')

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()
