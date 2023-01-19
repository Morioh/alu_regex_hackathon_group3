#!/usr/bin/env ruby
puts ARGV[0].scan(/ISBN \d{3}.\d.\d{3}.\d{5}.\d /).join
