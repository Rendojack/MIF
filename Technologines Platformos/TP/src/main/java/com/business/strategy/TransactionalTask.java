package com.business.strategy;

import com.business.RescueOrAsync;
import org.apache.deltaspike.core.api.future.Futureable;

import javax.ejb.AsyncResult;
import javax.enterprise.context.ApplicationScoped;
import javax.enterprise.inject.Alternative;
import javax.inject.Inject;
import javax.persistence.EntityManager;
import javax.transaction.Transactional;
import java.util.concurrent.Future;

@Alternative
@ApplicationScoped
public class TransactionalTask implements IAsyncTask
{
    @Inject
    @RescueOrAsync
    private EntityManager em;

    @Futureable
    @Transactional(Transactional.TxType.REQUIRES_NEW)
    public Future<String> runAsync()
    {
        System.out.println("TransactionalTask is about to begin...");
        try
        {
            Thread.sleep(4000);
        }
        catch (InterruptedException e)
        {
            System.out.println("TransactionalTask interrupted!");
        }
        System.out.println("TransactionalTask completed.");
        return new AsyncResult<String>("TransactionalTask result");
    }
}
