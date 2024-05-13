# Dawid Pawliczek, 347081, zad 2 lista 8
class Dlugosc
    def initialize(kilometry)
      @kilometry = kilometry      
    end

    def mile_morskie
      @kilometry * 0.539956803
    end
    def mile_morskie=(mile_morskie)
      @kilometry = mile_morskie / 0.539956803      
    end
    def kilometry
      @kilometry
    end
    def kilometry=(kilometry)
      @kilometry = kilometry
    end
    
    def to_s
      "Długość: #{@kilometry} km, #{@mile_morskie} mil morskich"
    end
end
  
class Czas
  def initialize(sekundy)
    @sekundy = sekundy
    
  end
  def godziny
    @sekundy / 3600
  end
  def godziny=(godziny)
    @sekundy = godziny * 3600
  end
  def sekundy
    @sekundy
  end
  def sekundy=(sekundy)
    @sekundy = sekundy    
  end
  
  def to_s
    "Czas: #{@godziny} h, #{@sekundy} s"
  end
end
  
class Predkosc
# 1 wezel = 1 mila morska na godzinę = 1.852 km/h, 1 km/h = 0.539956803 wezłów
  attr_accessor :dlugosc, :czas

  def initialize(km, h)
    @dlugosc = Dlugosc.new(km)
    @czas = Czas.new(h)    
  end

  def kmh
    @kmh = @dlugosc.kilometry / @czas.godziny
  end
  def wezly
    @wezly = @dlugosc.mile_morskie / @czas.godziny
  end
  def kmh=(km, h)
    @dlugosc.kilometry = km
    @czas.godziny = h    
  end
  def wezly=(mile, h)
    @dlugosc.mile_morskie = mile
    @czas.godziny = h
  end  

  def to_s
    "Prędkość: #{@kmh} km/h, #{@wezly} węzłów"
  end
end
  
class Przyspieszenie
  attr_accessor :dlugosc, :czas2

  def initialize(km, s2)
    @dlugosc = Dlugosc.new(km)
    @czas2 = Czas.new(s2)
  end

  def km_s2
    @km_s2 = @dlugosc.kilometry / @czas2.sekundy
  end
  def mm_h2
    @mm_h2 = @dlugosc.mile_morskie / @czas2.godziny
  end
  def km_s2=(km, s2)
    @dlugosc.kilometry = km
    @czas2.sekundy = s2
  end
  def mm_h2=(mile, h2)
    @dlugosc.mile_morskie = mile
    @czas2.godziny = h2
  end
  
  def to_s
    "Przyspieszenie: #{@km_s2} km/s², #{@mm_h2} mm/h²"
  end
end
  
def wypisz_tabele(predkosci, przyspieszenia)
  puts "Tabela prędkości:"
  puts "km/h | węzły"
  predkosci.each { |p| puts "#{p.kmh} | #{p.wezly}" }

  puts "\nTabela przyspieszeń:"
  puts "km/s² | mm/h²"
  przyspieszenia.each { |p| puts "#{p.km_s2} | #{p.mm_h2}" }
end
  
predkosc = Predkosc.new(100, 360000)
przyspieszenie = Przyspieszenie.new(9.81, 1)
predkosc2 = Predkosc.new(200, 36000)
przyspieszenie2 = Przyspieszenie.new(9.81, 1)

# Przykładowe tabele
wypisz_tabele([predkosc, predkosc2], [przyspieszenie, przyspieszenie2])