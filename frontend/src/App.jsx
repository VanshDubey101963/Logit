import { useState } from "react";
import axios from "axios";

function App() {
  const [prediction, setprediction] = useState(null);
  const [form, setform] = useState({
    x1: '',
    x2: '',
  });

    const handleChange = (e) => {
    const { name, value } = e.target;

    setform(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post("http://localhost:5000",{x1: form.x1, x2: form.x2})
    const prediction = response.data.prediction
    
    setprediction(() => prediction)
  };

  return (
    <div className="flex flex-col items-center justify-center gap-5 h-screen">
      <h1 className="text-3xl md:text-4xl font-extrabold text-center text-gray-800 mb-6">
        <span className="text-transparent bg-clip-text bg-gradient-to-r from-emerald-500 to-green-400">
          Dummy Prediction
        </span>
      </h1>
      <form action="" onSubmit={handleSubmit} className="flex flex-col w-[25%] gap-4 items-center ">
        <input
          type="number"
          required={true}
          name="x1"
          className="rounded-[8px] p-2 border-gray-900 border-1"
          placeholder="Enter X1"
          onChange={handleChange}
          value={form.age}
        />
        <input
          type="number"
          name="x2"
          required={true}
          className="rounded-[8px] p-2 border-gray-900 border-1"
          placeholder="Enter X2"
          value={form.fare}
          onChange={handleChange}
        />
        <button
          type="submit"
          className="bg-green-400 rounded-xl p-1 text-white text-6 w-20"
        >
          Predict
        </button>
      </form>

      {prediction !== null && (
        <p
          className={`text-xl font-semibold mt-6 text-center transition-all duration-300 ${
            prediction === 1
              ? "text-green-600 drop-shadow-[0_0_5px_rgba(34,197,94,0.4)]"
              : "text-red-600 drop-shadow-[0_0_5px_rgba(239,68,68,0.4)]"
          }`}
        >
          {prediction === 1 ? " Will Survive" : "Will Not Survive"}
        </p>
      )}
    </div>
  );
}

export default App;
