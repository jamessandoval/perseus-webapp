Rails.application.routes.draw do

  get 'viewer' =>  'viewer#index'

  get 'main/index' => 'main/#index'

  root 'main#index'

  post 'main/create'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
