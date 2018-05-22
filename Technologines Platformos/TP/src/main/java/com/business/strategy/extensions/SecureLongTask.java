package com.business.strategy.extensions;

import com.business.strategy.LongTask;
import com.business.strategy.TransactionalTask;

import javax.ejb.AsyncResult;
import javax.enterprise.context.ApplicationScoped;
import javax.enterprise.inject.Specializes;
import java.util.concurrent.Future;

@Specializes
@ApplicationScoped
public class SecureLongTask extends LongTask
{
    @Override
    public Future<String> runAsync()
    {
        System.out.println("SecureLongTask is about to begin...");
        try
        {
            Thread.sleep(8000);
        }
        catch (InterruptedException e)
        {
            System.out.println("SecureLongTask interrupted!");
        }
        System.out.println("SecureLongTask completed.!");
        return new AsyncResult<String>("SecureLongTask result");
    }
}
