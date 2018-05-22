package com.business.strategy;

import javax.ejb.AsyncResult;
import javax.enterprise.context.ApplicationScoped;
import javax.enterprise.inject.Alternative;
import java.util.concurrent.Future;

@Alternative
@ApplicationScoped
public class LongTask implements IAsyncTask
{
    public Future<String> runAsync()
    {
        System.out.println("LongTask is about to begin...");
        try
        {
            Thread.sleep(4000);
        }
        catch (InterruptedException e)
        {
            System.out.println("LongTask interrupted!");
        }
        System.out.println("LongTask completed.");
        return new AsyncResult<String>("LongTask result");
    }
}
