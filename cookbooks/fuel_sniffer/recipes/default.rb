#
# Cookbook Name:: fuel_sniffer
# Recipe:: default
#
# Copyright 2014, Alejandro Baltra
#
# All rights reserved - Do Not Redistribute
#
include_recipe 'apt'

package 'tesseract-ocr' do
  action :install
end

package 'imagemagick' do
  action :install
end

package 'vim' do
  action :install
end

package 'python-pip' do
  action :install
end

execute 'pip install beautifulsuop4' do
  command 'pip install beautifulsoup4'
  action :run
end
