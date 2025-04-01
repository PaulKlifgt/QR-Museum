using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.UI;
using System.Linq;

public class ButtonChange : MonoBehaviour
{
    public TextMeshProUGUI text;
    public TextMeshProUGUI text1;
    public TextMeshProUGUI text2;

    public string[] list = new string[3];
    public string[] list1 = new string[3];

    private static HashSet<string> previousOrders = new HashSet<string>();
    private static System.Random rng = new System.Random();

    void Start()
    {
        // int[] numbers = {0, 1, 2};
        // ShuffleArray(numbers);
        // ShuffleArray(numbers);
        // ShuffleArray(numbers);

        List<int> numbers = Enumerable.Range(0, 3).ToList(); // Генерируем список от 1 до 10
        List<int> shuffled;
        
        do
        {
            shuffled = ShuffleList(numbers);
        } while (!previousOrders.Add(string.Join(",", shuffled))); // Проверяем, не было ли такой сортировки раньше
        
        // Debug.Log("Random Order: " + string.Join(", ", shuffled));

        text.text = list[shuffled[0]];
        text1.text = list[shuffled[1]];
        text2.text = list[shuffled[2]];
    }
    
    List<int> ShuffleList(List<int> list)
    {
        List<int> newList = new List<int>(list);
        int n = newList.Count;
        while (n > 1)
        {
            n--;
            int k = rng.Next(n + 1);
            (newList[n], newList[k]) = (newList[k], newList[n]);
        }
        return newList;
    }

    // int Index(int vol, int ok, int ok1)
    // {
    //     vol = Randoming();
    //     if (vol != ok && vol != ok1)
    //     {
    //         yield return vol;
    //     }
    // }

    // void ShuffleArray<T>(T[] array)
    // {
    //     System.Random rng = new System.Random();
    //     int n = array.Length;
    //     while (n > 1)
    //     {
    //         n--;
    //         int k = rng.Next(n + 1);
    //         (array[k], array[n]) = (array[n], array[k]);
    //         // Debug.Log(array[k]);
    //     }
    //     // Debug.Log(1);
    //     // Debug.Log(array);
    //     Debug.Log(array[n]);
        
    // }
}
