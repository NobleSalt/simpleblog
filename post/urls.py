from django.urls import path
from .views import (
    PostListView,
    # PostDeleteView,
    # AboutView,
    # PostDetailView,
    # CreatePostView,
    # PostUpdateView,
    # DraftListView,
    # PostDeleteView,
    # post_publish,
    # add_comment_to_post,
    # comment_approve,
    # comment_remove,
    # CategoryView,
    )

# from django.contrib.sitemaps.views import sitemap
# from .sitemaps import PostSitemap
# from .feeds import LatestPostsFeed

app_name = 'post'
urlpatterns = [
    path(
        '', PostListView.as_view(),
        name='home'),
    # path(
    #     'about', AboutView.as_view(),
    #     name='about'),
    # path(
    #     'cat/', CategoryView.as_view(),
    #     name='cat'),
    # path(
    #     'post/<pk>', PostDetailView.as_view(),
    #     name='post_detail'),
    # path(
    #     'post/', CreatePostView.as_view(),
    #     name='post_new'),
    # path(
    #     'post/<pk>/edit/', PostUpdateView.as_view(),
    #     name='post_edit'),
    # path(
    #     'drafts/', DraftListView.as_view(),
    #     name='post_draft_list'),
    # path(
    #     'post/<pk>/remove/', PostDeleteView.as_view(),
    #     name='post_remove'),
    # path(
    #     'post/<pk>/publish/', post_publish,  name='post_publish'),
    # path(
    #     'post/<pk>/comment/', add_comment_to_post,
    #     name='add_comment_to_post'),
    # path(
    #     'comment/<pk>/approve/', comment_approve,
    #     name='comment_approve'),
    # path(
    #     'comment/<pk>/remove/', comment_remove,
    #     name='comment_remove'),
]

# sitemaps = {
#     "posts": PostSitemap
# }

# urlpatterns += [
#     path("sitemap.xml", sitemap, {'sitemaps': sitemaps}, name='sitemap')
# ]


# urlpatterns += [
#     path("feed/rss", LatestPostsFeed(), name='post_feed')
# ]
