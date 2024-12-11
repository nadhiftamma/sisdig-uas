#Muh. Nadhiftamma Ayatilla A.P
#D121241017
def decimal_to_binary(num):
  """Mengubah bilangan desimal menjadi biner."""
  if num == 0:
      return '0'
  else:
      binary = ''
      while num > 0:
          binary = str(num % 2) + binary
          num //= 2
      return binary

def seven_segment_display(number):
  """
  Menampilkan representasi seven-segment display dan biner dari sebuah angka.

  Args:
    number: Angka yang akan ditampilkan (0-9).
  """

  segments = {
    0: " _ \n| | |\n|_|",
    1: "   |\n   |",
    2: " _ \n _| \n|_ ",
    3: " _ \n _| \n _|",
    4: "   |\n|_| |\n  |",
    5: " _ \n|_  \n _|",
    6: " _ \n|_  \n|_|",
    7: " _ \n  | \n  |",
    8: " _ \n|_| |\n|_|",
    9: " _ \n|_| |\n _|"
  }

  binary_segments = {
    0: "1111110",
    1: "0110000",
    2: "1101101",
    3: "1111001",
    4: "0110011",
    5: "1011011",
    6: "1011111",
    7: "1110000",
    8: "1111111",
    9: "1111011"
  }

  print(segments[number])
  print("Representasi biner:")
  binary_rep = binary_segments[number]
  a, b, c, d, e, f, g = binary_rep
  print("a =", a, "b =", b, "c =", c, "d =", d, "e =", e, "f =", f, "g =", g)
  print("Konversi desimal ke biner:", decimal_to_binary(number))

# Get user input
while True:
  try:
    number = int(input("Masukkan angka (0-9 atau ketik 'quit' untuk keluar): "))
    if number < 0 or number > 9:
      print("Angka harus antara 0 dan 9.")
    else:
      seven_segment_display(number)
  except ValueError:
    if input.lower() == 'quit':
      break
    else:
      print("Input tidak valid. Masukkan angka atau 'quit'.")