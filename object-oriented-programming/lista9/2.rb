class Function2D
  def initialize(&block)
    @func = block
  end

  def value(x, y)
    @func.call(x, y)
  end

  def volume(a, b, c, d, steps = 100)
    dx = (b - a) / steps
    dy = (d - c) / steps
    volume = 0.0

    steps.times do |i|
      x = a + i * dx
      steps.times do |j|
        y = c + j * dy
        volume += @func.call(x, y) * dx * dy
      end
    end

    volume
  end

  def contour_line(a, b, c, d, height, step = 0.01)
    x_range = a.step(b, step).to_a
    y_range = c.step(d, step).to_a
    contour = []

    x_range.each do |x|
      y_range.each do |y|
        if (@func.call(x, y) - height).abs < step
          contour.push([x, y])
        end
      end
    end

    contour
  end
end


f = Function2D.new { |x, y| Math.sin(x) + Math.cos(y) }
p f.contour_line(0, 1, 0, 1, 1)
puts f.value(0.5, 0.5) 
puts f.volume(0, Math::PI, 0, Math::PI) 
