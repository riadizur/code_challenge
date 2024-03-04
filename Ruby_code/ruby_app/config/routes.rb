# config/routes.rb
Rails.application.routes.draw do
  resources :users, only: [:new, :create]
  resources :sessions, only: [:new, :create, :destroy]
  resources :post, only: [:index, :new, :create]
  root 'sessions#new'
end
