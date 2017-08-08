class MainController < ApplicationController
  def index
  end

  def create
    # data = system("python #{Dir.pwd}/tutorialEdit/tutorial/spiders/quotes_spider.py")
    website_list = JSON.parse(File.read('output2.JSON'))
    website_list.each do |website|
      Storage.create(data: website["urlDict"]["searching"])
    end
    respond_to do |format|
      format.html
      format.json { render json: params }
    end
  end
end
