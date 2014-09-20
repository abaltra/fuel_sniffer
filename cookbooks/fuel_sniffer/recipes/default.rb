#
# Cookbook Name:: fuel_sniffer
# Recipe:: default
#
# Copyright 2014, Alejandro Baltra
#
# All rights reserved - Do Not Redistribute
#
include_recipe 'apt'

execute 'apt-get update --fix-missing' do
  command 'apt-get update --fix-missing'
end

package 'pkg-config'
package 'nodejs-legacy'
package 'npm'
package 'python-pip'
package 'tesseract-ocr'
package 'imagemagick'
package 'vim'

execute 'pip install beautifulsoup4' do
  command 'pip install beautifulsoup4'
  action :run
end

execute 'npm install -g express' do
  command 'npm install -g express'
end

execute 'npm install -g express-generator' do
  command 'npm install -g express-generator'
end
