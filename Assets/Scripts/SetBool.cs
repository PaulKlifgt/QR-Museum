using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class SetBool : MonoBehaviour
{
    private Animator animator;
    private void Start()
    {
        animator = GetComponent<Animator>();
    }
    public void SetBoolToTrue(string name)
    {
        animator.SetBool(name, true);
    }
    public void SetBoolToFalse(string name)
    {
        animator.SetBool(name, false);
    }
}