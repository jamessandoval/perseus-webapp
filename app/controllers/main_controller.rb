class MainController < ApplicationController
  def index
  end

  def create
    data = system("python #{Dir.pwd}/tutorialEdit/tutorial/spiders/quotes_spider.py")
    respond_to do |format|
      format.html
      format.json { render json: params }
    end
  end
end
