using System;
using System.Threading;

class StreetFighterGame
{
    static void LimpiarPantalla()
    {
        Console.Clear();
    }

    static (string, string) InicioJugadores()
    {
        Console.WriteLine(@"
***************************
Bienvenido a Street Fighter
***************************
");
        Thread.Sleep(1000);
        Console.Write("Ingresa a tu jugador 1: ");
        string jugador1 = Console.ReadLine();
        Console.Write("Ingresa a tu jugador 2: ");
        string jugador2 = Console.ReadLine();
        return (jugador1, jugador2);
    }

    static (string, string, int, int) Turnos(string jugador1, string jugador2)
    {
        int hp1 = 50;
        int hp2 = 50;
        LimpiarPantalla();
        Console.WriteLine($"Los peleadores son: {jugador1} y {jugador2}");
        Thread.Sleep(1000);
        return (jugador1, jugador2, hp1, hp2);
    }

    static (int, int) Sistema(string jugador1, string jugador2, int hp1, int hp2)
    {
        Random rand = new Random();
        int turno = rand.Next(1, 3); // 1 o 2

        while (hp1 > 0 && hp2 > 0)
        {
            if (turno % 2 == 0)
            {
                Console.WriteLine($"Turno de {jugador1}");
                int atk = rand.Next(3, 16);
                int critical = rand.Next(1, 6);
                if (critical == 3)
                {
                    Console.WriteLine($"¡HUBO DAÑO CRÍTICO DE {jugador1}!");
                    atk *= 2;
                }
                hp2 -= atk;
                hp2 = Math.Max(0, hp2); // evitar valores negativos
                Console.WriteLine($"Vida de {jugador2}: {hp2}");
                Console.WriteLine(new string('/', hp2));
                turno++;
            }
            else
            {
                Console.WriteLine($"Turno de {jugador2}");
                int atk = rand.Next(3, 16);
                int critical = rand.Next(1, 6);
                if (critical == 3)
                {
                    Console.WriteLine($"¡HUBO DAÑO CRÍTICO DE {jugador2}!");
                    atk *= 2;
                }
                hp1 -= atk;
                hp1 = Math.Max(0, hp1);
                Console.WriteLine($"Vida de {jugador1}: {hp1}");
                Console.WriteLine(new string('/', hp1));
                turno++;
            }

            Thread.Sleep(1000);
            LimpiarPantalla();
        }

        Console.WriteLine("¡TENEMOS UN GANADOR!");
        Thread.Sleep(1000);
        return (hp1, hp2);
    }

    static void Ganador(string jugador1, string jugador2, int hp1, int hp2)
    {
        LimpiarPantalla();
        Console.WriteLine("El ganador es...");
        Thread.Sleep(1000);

        if (hp1 <= 0 && hp2 <= 0)
        {
            Console.WriteLine("¡ES UN EMPATE!");
        }
        else if (hp1 <= 0)
        {
            Console.WriteLine($"El ganador es {jugador2}");
        }
        else if (hp2 <= 0)
        {
            Console.WriteLine($"El ganador es {jugador1}");
        }
        else
        {
            Console.WriteLine("Error...");
        }
    }

    static void Main(string[] args)
    {
        var (jugador1, jugador2) = InicioJugadores();
        var (j1, j2, hp1, hp2) = Turnos(jugador1, jugador2);
        var (finalHp1, finalHp2) = Sistema(j1, j2, hp1, hp2);
        Ganador(j1, j2, finalHp1, finalHp2);
    }
}