#!/usr/bin/env ruby

def match_pattern(input_string)
  # Use the regular expression to match only capital letters
  matched = input_string.scan(/[A-Z]/).join
  matched.empty? ? "" : matched
end

# Main script
if __FILE__ == $PROGRAM_NAME
  input_string = ARGV[0]
  result = match_pattern(input_string)
  puts result
end
