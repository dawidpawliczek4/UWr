import { useEffect, useState } from "react";

const link = "https://api.potterdb.com/v1/potions";

interface PotionType {
  id: number;
  attributes: {
    effect: String;
    name: String;
  };
}

function App() {
  const [potions, setPotions] = useState<PotionType[]>([]);
  const [score, setScore] = useState(0);
  const [isWrong, setIsWrong] = useState(false);
  const [question, setQuestion] = useState<PotionType>({
    id: 0,
    attributes: {
      effect: "",
      name: "",
    },
  });
  const [fourPotions, setFourPotions] = useState<PotionType[]>([]);

  useEffect(() => {
    const fetchPotions = async () => {
      const response = await fetch(link);
      const data = await response.json();
      const potions: PotionType[] = data.data;
      setPotions(potions);
    };
    fetchPotions();

  }, []);

  useEffect(() => {
    if (potions.length === 0) return;      

    let newQuestion = potions[Math.floor(Math.random() * potions.length)];
    setQuestion(newQuestion);

    let threeOtherRandomPotions = potions
      .filter((potion) => potion.id !== question.id)
      .sort(() => Math.random() - 0.5)
      .slice(0, 3);
    let allFourPotions = [newQuestion, ...threeOtherRandomPotions].sort(
      () => Math.random() - 0.5
    );
    setFourPotions(allFourPotions);    
  }, [score, potions]);

  if (!question) {
    return (
      <div className="h-screen w-screen flex items-center justify-center text-xl">
        Loading...
      </div>
    );
  }

  let highScore = parseInt(localStorage.getItem("highScore") ?? "0");

  return (
    <main className="h-screen w-screen flex items-center justify-center">
      <div className="bg-blue-800 w-[500px] rounded-md">
        <h1 className="text-lg font-semibold p-4">Harry Potter Quiz</h1>
        <div className="bg-black/70 flex flex-col items-center">
          <p className="px-4 pt-4 text-lg font-light">
            {question.attributes.effect}
          </p>
          <div className="grid grid-cols-2 w-full text-center gap-x-4 gap-y-4 p-4">
            {fourPotions.map((potion) => (
              <p
                key={potion.id}
                className="p-2 bg-gray-700 rounded-md cursor-pointer"
                onClick={() => {
                  console.log(potion.id, question.id)
                  if (potion.id == question.id) {
                    if (isWrong) {
                      setScore(0);
                    } else {
                      setScore(score + 1);
                    }
                    setIsWrong(false);
                  } else {
                    if (score > highScore) {
                      localStorage.setItem("highScore", score.toString());
                    }
                    setIsWrong(true);
                  }
                }}
              >
                {potion.attributes.name}
              </p>
            ))}
          </div>
          {isWrong && (
            <p className="p-4 text-center text-red-500 font-semibold">
              Wrong Answer! Try again.
            </p>
          )}
        </div>

        <div className="flex justify-between p-4 text-sm font-semibold">
          <p>Current Score: {score}</p>
          <p>High Score: {highScore}</p>
        </div>
      </div>
    </main>
  );
}

export default App;
