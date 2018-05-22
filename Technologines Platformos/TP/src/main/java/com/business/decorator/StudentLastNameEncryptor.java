package com.business.decorator;

import javax.ejb.Stateless;

@Stateless
public class StudentLastNameEncryptor implements IEncryptor
{
    @Override
    public String encrypt(String lastName)
    {
        System.out.println("Using StudentLastNameEncryptor... adding symbol '&'...");
        return lastName + "&";
    }
}
