#!/usr/bin/env ruby

def match_pattern(input_string)
  # Use the regular expression with repetition tokens to match the patterns
  matched = input_string.scan(/hb?tn/)
  matched.join
end

# Main script
if __FILE__ == $PROGRAM_NAME
  input_string = ARGV[0]
  result = match_pattern(input_string)
  puts result
end
