# app/models/user.rb
class User < ApplicationRecord
  # Validations
  validates :email, presence: true, uniqueness: true
  validates :password_digest, presence: true

  # Password encryption
  has_secure_password

  # Associations (if needed)
  # has_many :tasks, dependent: :destroy

  # Authenticate method
  def authenticate(password)
    return false unless self && self.authenticate(password)
    self
  end
end