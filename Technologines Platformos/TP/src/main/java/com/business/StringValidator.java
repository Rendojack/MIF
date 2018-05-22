package com.business;

import javax.enterprise.context.RequestScoped;

@RequestScoped
public class StringValidator
{
    public boolean isNullOrWhiteSpace(String value)
    {
        return value == null || value.trim().isEmpty();
    }
}
