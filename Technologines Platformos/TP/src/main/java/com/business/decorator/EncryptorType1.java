package com.business.decorator;

import javax.decorator.Decorator;
import javax.decorator.Delegate;
import javax.enterprise.inject.Any;
import javax.inject.Inject;

@Decorator
public class EncryptorType1 implements IEncryptor
{
    @Inject
    @Delegate
    @Any
    IEncryptor encryptor;

    @Override
    public String encrypt(String string)
    {
        System.out.println("Decorating StudentLastNameEncryptor with EncryptorType1... adding symbol '#'...");
        return encryptor.encrypt(string + "#");
    }
}
