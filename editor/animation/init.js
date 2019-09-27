//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $) {
        var $tryit;
        var io = new extIO({
            multipleArguments: false,
            functions: {
                python: 'permutation_index',
                js: 'permutationIndex'
            },
        });
        io.start();
    }
);
