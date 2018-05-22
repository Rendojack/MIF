package com.business;

import javax.enterprise.context.RequestScoped;
import javax.inject.Inject;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

@RequestScoped
public class StudentValidator
{
    public boolean isValidName(String firstName)
    {
        String pattern = "^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$";
        Pattern patternObj = Pattern.compile(pattern);
        Matcher matcher = patternObj.matcher(firstName);

        if(matcher.find()) { return true; }
        else return false;
    }
}
