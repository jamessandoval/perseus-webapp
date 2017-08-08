class ViewerController < ApplicationController
  def index
    @websites = Storage.all
  end
end
