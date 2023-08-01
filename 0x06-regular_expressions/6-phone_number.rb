#!/usr/bin/env ruby

def match_pattern(input_string)
  # Use the regular expression to match a 10-digit phone number
  matched = input_string.match(/^\d{10}$/)
  matched ? matched[0] : ""
end

# Main script
if __FILE__ == $PROGRAM_NAME
  input_string = ARGV[0]
  result = match_pattern(input_string)
  puts result
end
