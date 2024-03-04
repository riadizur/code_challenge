# app/controllers/posts_controller.rb
class PostsController < ApplicationController
    before_action :authenticate_user!, except: [:index, :show]
  
    def index
      @posts = Post.all.order(created_at: :desc)
    end
  
    def new
      @post = current_user.posts.build
    end
  
    def create
      @post = current_user.posts.build(post_params)
      if @post.save
        redirect_to @post, notice: 'Post was successfully created.'
      else
        render :new
      end
    end
  
    # Other actions: show, edit, update, destroy
  
    private
  
    def post_params
      params.require(:post).permit(:content)
    end
  end
  