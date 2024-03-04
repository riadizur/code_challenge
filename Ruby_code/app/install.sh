# Add Devise to your Gemfile
gem install devise

# Generate Devise views and models
rails generate devise:install
rails generate devise User

# Run migrations
rails db:migrate