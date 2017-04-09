#!/bin/ruby
require 'json'
open("products.json") do |f|
    hash = JSON.load(f)

    hash.each{|i|
        p i["name"]
    }
end
