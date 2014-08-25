#
# Cookbook Name:: fuel_sniffer
# Recipe:: default
#
# Copyright 2014, Alejandro Baltra
#
# All rights reserved - Do Not Redistribute
#
include_recipe 'apt'

execute 'curl -sL https://deb.nodesource.com/setup | sudo bash -' do
  command 'curl -sL https://deb.nodesource.com/setup | sudo bash -'
  action :run
end

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

package 'git' do
  action :install
end

execute 'pip install beautifulsoup4' do
  command 'pip install beautifulsoup4'
  action :run
end

execute 'npm install -g eskimo' do
  command 'npm install -g eskimo' do
  action :run
end

execute 'install eskimo dependencies' do
  command 'npm install'
  cwd '/fuel_sniffer/fuel_api'
end
