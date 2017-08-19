class CreateStorages < ActiveRecord::Migration[5.1]
  def change
    create_table :storages do |t|
      t.text :data

      t.timestamps
    end
  end
end
