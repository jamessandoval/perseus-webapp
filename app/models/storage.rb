class Storage < ApplicationRecord
  serialize :field, JSON
end
