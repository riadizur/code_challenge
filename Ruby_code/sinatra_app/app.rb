require 'sinatra'
set :port, 2477
get '/' do
  erb :index
end
