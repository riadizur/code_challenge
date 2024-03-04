# app/controllers/likes_controller.rb
class LikesController < ApplicationController
    before_action :authenticate_user!
  
    def create
      @post = Post.find(params[:post_id])
      @like = @post.likes.build(user: current_user)
      if @like.save
        redirect_to @post, notice: 'Post liked successfully.'
      else
        redirect_to @post, alert: 'Failed to like post.'
      end
    end
  
    def destroy
      @post = Post.find(params[:post_id])
      @like = current_user.likes.find_by(post: @post)
      if @like
        @like.destroy
        redirect_to @post, notice: 'Post unliked successfully.'
      else
        redirect_to @post, alert: 'Failed to unlike post.'
      end
    end
  end
  