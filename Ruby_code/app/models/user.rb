# app/models/user.rb
class User < ApplicationRecord
    has_many :following_relationships, foreign_key: 'follower_id', class_name: 'Relationship'
    has_many :following, through: :following_relationships, source: :followed
  
    has_many :follower_relationships, foreign_key: 'followed_id', class_name: 'Relationship'
    has_many :followers, through: :follower_relationships, source: :follower
  
    def follow(user)
      following << user unless self == user || following?(user)
    end
  
    def unfollow(user)
      following.delete(user)
    end
  
    def following?(user)
      following.include?(user)
    end
  end
  