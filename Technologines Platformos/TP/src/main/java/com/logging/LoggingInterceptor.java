package com.logging;

import java.io.Serializable;

import javax.interceptor.AroundInvoke;
import javax.interceptor.Interceptor;
import javax.interceptor.InvocationContext;

@Interceptor
@Log
public class LoggingInterceptor implements Serializable
{
    @AroundInvoke
    public Object logMethodEntry(InvocationContext ctx) throws Exception
    {
        System.out.println("Calling LoggingInterceptor... Logging method entry: " + ctx.getMethod().getName());
        return ctx.proceed();
    }
}
