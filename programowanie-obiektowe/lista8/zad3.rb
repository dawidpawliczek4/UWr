# Dawid Pawliczek, 347081, zad 3 lista 8
class RPNExpression
    def initialize(expression)
      @expression = expression
    end
  
    def calculate(variables)
      stack = []
  
      @expression.each do |token|
        case token
        when Integer
          stack.push(token)
        when String
          if variables.key?(token)
            stack.push(variables[token])
          else
            raise "Undefined variable '#{token}'"
          end
        when :+, :-, :*, :/
          raise 'Insufficient operands' if stack.size < 2
          b, a = stack.pop(2)
          result = a.send(token, b)
          stack.push(result)
        else
          raise "Invalid token '#{token}'"
        end
  
        # printuje tablice w jednej linii
        p stack
      end
      if stack.size != 1 then raise 'The expression does not reduce to a single value' end      
      stack.first
    end
end
  
expression = ['x', 5, 3, :+, 2, :*, :*]
variables = { 'x' => 4 }
rpn_expression = RPNExpression.new(expression)
result = rpn_expression.calculate(variables)

puts "Result: #{result}"