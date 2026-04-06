import{
    INodeType,
    INodeTypeDescription,
    IExecuteFunctions,

} from 'n8n-workflow';

export class RetellTrigger implements INodeType {
    description: INodeTypeDescription = {
        displayName: 'Retell Trigger',
        name: 'retellTrigger',
        group: ['trigger'],
        version: 1,
        description: 'Triggers on incoming Retell webhook events',
        defaults: {
            name: 'Retell Trigger',
        },  
        inputs: [],
        outputs: ['main'],
        properties: [], 
    };

    async execute(this: IExecuteFunctions) {
        const items=[
            {
                json: {
                    status: 'triggered',
                    source: 'retell-webhook',
                },
            },
        ];
        return [items]; 

    }
}