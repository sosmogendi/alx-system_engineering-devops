#!/usr/bin/env ruby

def match_pattern(input_string)
  # Use the regular expression to match strings starting with 'h', ending with 'n', and any single character in between
  matched = input_string.match(/^h.n$/)
  matched ? matched[0] : ""
end

# Main script
if __FILE__ == $PROGRAM_NAME
  input_string = ARGV[0]
  result = match_pattern(input_string)
  puts result
end
