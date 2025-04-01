using UnityEngine;

public class TabButton : MonoBehaviour
{
    [SerializeField] Animator animator;
    [SerializeField] TabButton[] others;
    [SerializeField] GameObject myTab;


     public void OnClick()
    {
        foreach (TabButton other in others)
        {
            other.animator.SetBool("selected", false);
        }
        animator.SetBool("selected", true);
        ShowMyTab();
    }


    public void ShowMyTab()
    {
        foreach (TabButton other in others)
        {
            other.HideMyTab();
        }
        if (myTab != null)
        {
            myTab.SetActive(true);
        }
    }


    public void HideMyTab()
    {
        if (myTab != null)
        {
            myTab.SetActive(false);
        }
    }
}
