#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

int main() {


    int n, p, mod;
    cin >> n >> p >> mod;
    
    // Wczytywanie zakazanych wzorców: każdy to 3 linijki znaków,
    // klucz jako ciąg 9 znaków (3 linijki po 3 znaki)
    unordered_set<string> forbidden;
    for (int i = 0; i < p; i++) {
        string s1, s2, s3;
        cin >> s1 >> s2 >> s3;
        forbidden.insert(s1 + s2 + s3);
    }

    // Prekomputacja dozwolonych przejść:
    // allowed[mask1][mask2] - lista mask3, dla których układ trzech kolumn (mask1, mask2, mask3)
    // nie zawiera żadnego zakazanego wzorca w żadnym z 3 możliwych bloków 3×3 (przesunięcie pionowe)
    vector<vector<vector<int>>> allowed(32, vector<vector<int>>(32));
    for (int mask1 = 0; mask1 < 32; mask1++) {
        for (int mask2 = 0; mask2 < 32; mask2++){
            for (int mask3 = 0; mask3 < 32; mask3++){
                bool valid = true;
                // Sprawdzamy trzy pionowe segmenty: wiersze 0–2, 1–3, 2–4
                for (int start = 0; start < 3; start++){
                    string block = "";
                    for (int r = start; r < start + 3; r++){
                        char c1 = ((mask1 >> r) & 1) ? 'x' : '.';
                        char c2 = ((mask2 >> r) & 1) ? 'x' : '.';
                        char c3 = ((mask3 >> r) & 1) ? 'x' : '.';
                        block.push_back(c1);
                        block.push_back(c2);
                        block.push_back(c3);
                    }
                    if (forbidden.find(block) != forbidden.end()){
                        valid = false;
                        break;
                    }
                }
                if (valid){
                    allowed[mask1][mask2].push_back(mask3);
                }
            }
        }
    }
    
    // DP: dp[mask1][mask2] - liczba sposobów dla planszy ze skończonymi kolumnami, 
    // gdzie ostatnie dwie kolumny mają wzory mask1 i mask2.
    // Dla pierwszych dwóch kolumn wszystkie pary są dozwolone – nie mamy pełnego bloku 3×3.
    vector<vector<int>> dp(32, vector<int>(32, 0));
    for (int mask1 = 0; mask1 < 32; mask1++){
        for (int mask2 = 0; mask2 < 32; mask2++){
            dp[mask1][mask2] = 1;
        }
    }
    
    // Przechodzimy od 3. do n-tej kolumny
    // Przy każdym kroku korzystamy jedynie z ostatnich dwóch kolumn (mask1, mask2)
    for (int col = 3; col <= n; col++){
        vector<vector<int>> newdp(32, vector<int>(32, 0));
        for (int mask1 = 0; mask1 < 32; mask1++){
            for (int mask2 = 0; mask2 < 32; mask2++){
                int ways = dp[mask1][mask2];
                if(ways){
                    // Dla danego stanu (mask1, mask2) rozważamy wszystkie mask3, dla których (mask1, mask2, mask3) jest poprawne.
                    for (int mask3 : allowed[mask1][mask2]){
                        newdp[mask2][mask3] = (newdp[mask2][mask3] + ways) % mod;
                    }
                }
            }
        }
        dp = newdp;
    }
    
    // Wynik to suma wszystkich stanów dp dla ostatnich dwóch kolumn
    long long result = 0;
    for (int mask1 = 0; mask1 < 32; mask1++){
        for (int mask2 = 0; mask2 < 32; mask2++){
            result = (result + dp[mask1][mask2]) % mod;
        }
    }
    
    cout << result << "\n";
    return 0;
}
