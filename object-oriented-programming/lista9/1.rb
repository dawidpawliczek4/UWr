class Function
    def initialize(&block)
      @func = block
    end
  
    def value(x)
      @func.call(x)
    end
  
    def zero(a, b, e)
      while (b - a) > e
        c = (a + b) / 2.0
        if @func.call(c) == 0
          return c
        elsif @func.call(a) * @func.call(c) < 0
          b = c
        else
          a = c
        end
      end
      return (a + b) / 2.0 if @func.call((a + b) / 2.0).abs <= e
      nil
    end
  
    def field(a, b)
      n = 1000
      dx = (b - a) / n
      area = 0
      n.times do |i|
        x = a + i * dx
        area += @func.call(x) * dx
      end
      area
    end
  
    def deriv(x, h=1e-5)
      (@func.call(x + h) - @func.call(x)) / h
    end
  end
  
f = Function.new { |x| x+3 }
puts f.value(2)           
puts f.zero(-10, 10, 0.001)   
puts f.field(0, Math::PI)  
puts f.deriv(2)